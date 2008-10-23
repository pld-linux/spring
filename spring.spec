%define	subver	b5
Summary:	Powerful RTS engine
Name:		spring
Version:	0.77
Release:	0.%{subver}.1
License:	GPL v2
Group:		X11/Applications/Games/Strategy
Source0:	http://spring.clan-sy.com/dl/%{name}_%{version}%{subver}_src.tar.bz2
# Source0-md5:	3d2c3c879e4d07c1c2ca8c5181bf0a45
URL:		http://spring.clan-sy.com/
BuildRequires:	DevIL-devel >= 1.6.8-0.rc2
BuildRequires:	OpenAL-devel
BuildRequires:	boost-devel >= 1.34
BuildRequires:	cmake >= 1.6
BuildRequires:	freetype-devel
BuildRequires:	glew-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python-devel
BuildRequires:	rpm-javaprov
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powerful RTS engine.

Features:
- Large battles limited only by the power of computer; support for up
  to 5000 units.
- Large, highly detailed maps in which to wage those battles, fully 3D
  with deformable terrain, forest fires, dynamic and reflective water,
  and custom skyboxes.
- Several camera modes, allowing for anything to be viewed from almost
  any angle.
- Fully 3D combat in land, sea, and air, with realistic weapon
  trajectories (physics engine).
- Many different Games, made just for Spring.
- Complex 3rd party AIs, some of which are quite good.
- An extremely powerful GUI, designed to minimize unnecessary
  micromanagement.
- Frequent additions and bugfixes.

%prep
%setup -q -n %{name}_%{version}%{subver}

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIBDIR=%{_lib} \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-dedicated
%attr(755,root,root) %{_libdir}/libspringserver.so
%attr(755,root,root) %{_libdir}/libunitsync.so
%{_datadir}/games/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/application-x-spring-demo.png
