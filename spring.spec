#
# TODO: check unpackaged files
#
Summary:	Powerful RTS engine
Summary(pl.UTF-8):	Potężny silnik RTS
Name:		spring
Version:	0.81.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/springrts/spring-0.80.5/%{name}_%{version}_src.tar.gz
# Source0-md5:	d7e3b7c29e2375d94b6ab78dd83f2b8c
URL:		http://spring.clan-sy.com/
BuildRequires:	DevIL-devel >= 1.7.2-4
BuildRequires:	OpenAL-devel
BuildRequires:	SDL-devel
BuildRequires:	boost-devel >= 1.34
BuildRequires:	cmake >= 1.6
BuildRequires:	freetype-devel
BuildRequires:	glew-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	p7zip
BuildRequires:	which
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
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

%description -l pl.UTF-8
Potężny silnik RTS.

Funkcje:
- Wielkie bitwy ograniczone tylko mocą komputera; obsługa do 5000
  jednostek.
- Wielkie, szczegółowe mapy w których można przeprowadzać bitwy, w
  pełni trójwymiarowy teren, pożary lasów, dynamiczna i refleksyjna
  pogoda oraz definiowalne przez użytkownika chmury.
- Kilka trybów kamery, umożliwiające oglądanie każdego elementu prawie
  pod każdym kątem.
- W pełni trójwymiarowe walki na lądzie, morzu i w powietrzu,
  realistyczne trajketorie pocisków (zachowane prawa fizyki).
- Wiele przeróżnych gier, stworzonych wyłącznie dla Springa.
- Złożone systemy sztucznej inteligencji, niektóre z nich są całkiem
  dobre.
- Ekstremalnie potężne GUI, zaprojektowane w celu zminimalizowania
  niepotrzebnego mikrozarządzania.
- Często wypuszczane dodtaki oraz poprawki.

%prep
%setup -q -n %{name}_%{version}

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
