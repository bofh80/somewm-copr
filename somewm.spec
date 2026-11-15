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
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  lua-lgi
BuildRequires:  lua-lgi-compat
BuildRequires:  glslang
BuildRequires:  vulkan-headers
BuildRequires:  xorg-x11-server-Xwayland-devel
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)

Requires:       lua-lgi
Requires:       lua-lgi-compat
Requires:       xorg-x11-server-Xwayland

%description
SomeWM is a programmable Wayland compositor built on AwesomeWM's Lua
configuration model and wlroots.

%prep
%autosetup -n %{name}-%{version}

%build
%set_build_flags
meson setup %{_vpath_builddir} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --includedir=%{_includedir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --localedir=%{_localedir} \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --buildtype=plain \
    --wrap-mode=default
%meson_build

%install
%meson_install
rm -rf %{buildroot}%{_includedir}/wlroots-0.20
rm -f %{buildroot}%{_libdir}/libwlroots-0.20.a
rm -f %{buildroot}%{_libdir}/pkgconfig/wlroots-0.20.pc

if [ -f %{buildroot}/usr/etc/xdg/somewm/somewmrc.lua ]; then
    mkdir -p %{buildroot}/etc/xdg/somewm
    mv %{buildroot}/usr/etc/xdg/somewm/somewmrc.lua %{buildroot}/etc/xdg/somewm/
    rmdir -p --ignore-fail-on-non-empty %{buildroot}/usr/etc/xdg/somewm
fi


%files
%license LICENSE
%doc README.md
%dir /etc/xdg/somewm
%config(noreplace) /etc/xdg/somewm/somewmrc.lua
%{_bindir}/somewm
%{_bindir}/somewm-client
%{_libdir}/liblgi_closure_guard.so
%{_datadir}/somewm/
%{_datadir}/wayland-sessions/somewm.desktop
%{_datadir}/xdg-desktop-portal/portals/somewm.portal
%{_mandir}/man1/somewm*.1*





%changelog
* Sat Nov 14 2026 Builder <builder@example.com> - 2.1.2-1
- Initial package
