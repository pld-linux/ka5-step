#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		step
Summary:	step
Name:		ka5-%{kaname}
Version:	23.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fbbcbad3db784dbdbd341da15ed66bca
Patch0:		python.patch
URL:		http://www.kde.org/
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-khtml-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kplotting-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Step is an interactive physical simulator. It allows you to explore
the physical world through simulations.

Features

- Classical mechanical simulation in two dimensions
- Particles, springs with damping, gravitational and coulomb forces
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
- Errors calculation and propagation: you can enter values like "1.3 ±
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

%prep
%setup -q -n %{kaname}-%{version}
%patch0 -p1

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
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
