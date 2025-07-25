#
# Conditional build:
%bcond_with	tests		# testing

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		step
Summary:	Interactive physical simulator
Summary(pl.UTF-8):	Interaktywny symulator fizyczny
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	3
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f56500f0f96a02b633e9f326425fb833
Patch0:		python.patch
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	eigen3 >= 3.2.2
BuildRequires:	gettext-devel
BuildRequires:	gsl-devel >= 1.8
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kplotting-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libqalculate-devel >= 0.9.5
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Step is an interactive physical simulator. It allows you to explore
the physical world through simulations.

Features:
- Classical mechanical simulation in two dimensions
- Particles, springs with damping, gravitational and Coulomb forces
- Rigid bodies
- Collision detection (currently only discrete) and handling
- Soft (deformable) bodies simulated as user-editable
  particles-springs system, sound waves
- Molecular dynamics (currently using Lennard-Jones potential): gas
  and liquid, condensation and evaporation, calculation of macroscopic
  quantities and their variances
- Units conversion and expression calculation: you can enter something
  like "(2 days + 3 hours) * 80 km/h" and it will be accepted as
  distance value (requires libqalculate)
- Errors calculation and propagation: you can enter values like "1.3 +/-
  0.2" for any property and errors for all dependent properties will be
  calculated using statistical formulas
- Solver error estimation: errors introduced by the solver is
  calculated and added to user-entered errors
- Several different solvers: up to 8th order, explicit and implicit,
  with or without adaptive timestep (most of the solvers require the GSL
  library)
- Controller tool to easily control properties during simulation (even
  with custom keyboard shortcuts)
- Tools to visualize results: graph, meter, tracer
- Context information for all objects, integrated wikipedia browser
- Collection of example experiments, more can be downloaded with
  KNewStuff
- Integrated tutorials

%description -l pl.UTF-8
Step to interaktywny symulator fizyczny. Pozwala eksplorować świat
fizyczny poprzez symulacje.

Możliwości:
- klasyczna symulacja mechaniczna w dwóch wymiarach
- cząsteczki, sprężyny z tłumieniem, siły grawitacyjne i Coulomba
- bryły sztywne
- wykrywanie i obsługa kolizji (obecnie tylko dyskretnych)
- ciała miękkie (deformowalne) symulowane jako modyfikowalny przez
  użytkownika system cząstek-sprężyn, fale dźwiękowe
- dynamika molekularna (obecnie przy użyciu potencjału
  Lennarda-Jonesa): gazy i ciecze, kondensacja i parowanie, obliczenia
  wielkości kakroskopowych i ich wariancji
- przeliczanie jednostek o obliczanie wyrażeń: można wpisywać np.
  "(2 days + 3 hours) * 80 km/h" i zostanie to przyjęte jako wartość
  odległości (wymaga libqalculate)
- rachunek i propagowanie błędów: można wpisać np. "1.3 +/- 0.2" dla
  dowolnej własności, a błędy dla własności zależnych zostaną
  wyliczone przy użyciu wzorów statystycznych
- estymacja błędów rozwiązania: wprowadzane błędy są wyliczane i
  dodawane do błędów podanych przez użytkownika
- kilka różnych metod rozwiązywania: do 8. rzędu, jawna i niejawna, z
  lub bez kroku adaptacyjnego (większość wymaga biblioteki GSL)
- narzędzie kontrolera do sterowania własnościami podczas symulacji
  (nawet z własnymi skrótami klawiaturowymi)
- narzędzia do wizualizacji wyników: wykres, miernik, śledzenie
- informacje kontekstowe dla wszystkich obiektów, zintegrowana
  przeglądarka wikipedii
- zbiór przykładowych eksperymentów, więcej można pobrać przez
  KNewStuff
- zintegrowane instrukcje

%prep
%setup -q -n %{kaname}-%{version}
%patch -P0 -p1

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/step
%{_desktopdir}/org.kde.step.desktop
%{_datadir}/config.kcfg/step.kcfg
%{_iconsdir}/hicolor/128x128/apps/step.png
%{_iconsdir}/hicolor/16x16/apps/step.png
%{_iconsdir}/hicolor/22x22/actions/pointer.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Anchor.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Box.png
%{_iconsdir}/hicolor/22x22/actions/step_object_ChargedParticle.png
%{_iconsdir}/hicolor/22x22/actions/step_object_CircularMotor.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Controller.png
%{_iconsdir}/hicolor/22x22/actions/step_object_CoulombForce.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Disk.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Gas.png
%{_iconsdir}/hicolor/22x22/actions/step_object_GasParticle.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Graph.png
%{_iconsdir}/hicolor/22x22/actions/step_object_GravitationForce.png
%{_iconsdir}/hicolor/22x22/actions/step_object_LinearMotor.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Meter.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Note.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Particle.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Pin.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Polygon.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Rope.png
%{_iconsdir}/hicolor/22x22/actions/step_object_SoftBody.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Spring.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Stick.png
%{_iconsdir}/hicolor/22x22/actions/step_object_Tracer.png
%{_iconsdir}/hicolor/22x22/actions/step_object_WeightForce.png
%{_iconsdir}/hicolor/22x22/apps/step.png
%{_iconsdir}/hicolor/32x32/apps/step.png
%{_iconsdir}/hicolor/48x48/apps/step.png
%{_iconsdir}/hicolor/64x64/apps/step.png
%{_datadir}/metainfo/org.kde.step.appdata.xml
%{_datadir}/step
%{_datadir}/mime/packages/org.kde.step.xml
%{_datadir}/knsrcfiles/step.knsrc
