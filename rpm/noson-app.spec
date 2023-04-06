Name:           noson-app
Version:        5.4.0
Release:        0
Summary:        SONOS device controller
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://janbar.github.io/noson-app/index.html
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-qt5-qtquickcontrols2-devel >= 5.15.8
BuildRequires:  opt-qt5-qtsvg-devel >= 5.15.8
BuildRequires:  opt-qt5-qtbase-devel >= 5.15.8
BuildRequires:  pkgconfig(noson) >= 2.10.0
Requires:       qt-runner
Requires:       opt-qt5-qtquickcontrols2 >= 5.15.8
Requires:       opt-qt5-qtwayland >= 5.15.8
Requires:       opt-qt5-sfos-maliit-platforminputcontext
%{?opt_qt5_default_filter}

%description
A controller for SONOS devices. It allows for browsing the music
library, and playing tracks or radio on any zones. Zone groups,
queues and playlists can be managed, and playback be controlled.
%if 0%{?_chum}
PackageName: Noson
Type: desktop-application
DeveloperName: Jean-Luc Barrière
PackagerName: Adam Pigg
Categories:
 - Media
 - Audio
Custom:
  Repo: https://github.com/janbar/noson-app
  PackagingRepo: https://github.com/sailfishos-chum/noson-app
Icon: https://github.com/janbar/noson-app/raw/5.4.0/gui/icons/noson-128x128.png
%endif

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5 \
    -DBUILD_DEPENDENCIES=OFF \
    -DBUILD_LIBNOSON=OFF \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr/

%make_build

%install
%make_install -C build

#Add custom .desktop file
install -p -m644 -D ../io.github.janbar.noson.desktop %{buildroot}/%{_datadir}/applications/io.github.janbar.noson.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/noson-app
%{_datadir}/applications/io.github.janbar.noson.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/io.github.janbar.noson.appdata.xml
%{_libdir}/noson/
