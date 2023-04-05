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
BuildRequires:  opt-qt5-qtquickcontrols2-devel >= 5.15.8
BuildRequires:  opt-qt5-qtsvg-devel >= 5.15.8
BuildRequires:  opt-qt5-qtbase-devel >= 5.15.8
BuildRequires:  pkgconfig(noson) >= 2.10.0

%description
A controller for SONOS devices. It allows for browsing the music
library, and playing tracks or radio on any zones. Zone groups,
queues and playlists can be managed, and playback be controlled.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DEPENDENCIES=OFF \
    -DCMAKE_PREFIX_PATH:PATH=%{_opt_qt5_prefix} \
    -DBUILD_LIBNOSON=OFF
%make_build

%install
%make_install -C build


%files
%doc README.md
%license LICENSE
%{_bindir}/noson-app
%{_datadir}/applications/io.github.janbar.noson.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/io.github.janbar.noson.appdata.xml
%{_libdir}/noson/
