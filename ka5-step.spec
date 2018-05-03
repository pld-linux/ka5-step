%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		step
Summary:	step
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	91a3bf425879d9db49f9ea09c8b08462
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	eigen3
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
step.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/step.knsrc
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
%{_datadir}/kxmlgui5/step
%{_datadir}/metainfo/org.kde.step.appdata.xml
%{_datadir}/step
