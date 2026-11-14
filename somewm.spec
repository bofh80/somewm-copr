Name:           somewm
Version:        2.1.2
Release:        1%{?dist}
Summary:        A Lua framework for building your Wayland desktop

License:        GPL-3.0-or-later
URL:            https://github.com/trip-zip/somewm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  lua-lgi
BuildRequires:  lua-lgi-compat

Requires:       lua-lgi
Requires:       lua-lgi-compat
Requires:       xorg-x11-server-Xwayland

%description
SomeWM is a programmable Wayland compositor built on AwesomeWM's Lua
configuration model and wlroots.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson --wrap-mode=default
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/somewm
%{_bindir}/somewm-client
%{_datadir}/somewm/
%{_datadir}/wayland-sessions/somewm.desktop
%{_mandir}/man1/somewm*.1*
%{_userunitdir}/somewm*

%changelog
* Sat Nov 14 2026 Builder <builder@example.com> - 2.1.2-1
- Initial package
