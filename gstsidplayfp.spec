%define majorminor   0.10
%define gstreamer    gstreamer

%define gst_minver   0.10.16
%define gstpb_minver 0.10.16

Summary: GStreamer element for playback of SID files
Name: gst-siddecfp
Version: 0.10.0
Release: 1%{?dist}
License: GPLv2
Group: Applications/Multimedia
URL: https://github.com/oniongarlic/gst-siddecfp
Source: gstsidplayfp-%{version}.tar.gz
Requires: %{gstreamer} >= %{gst_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}
BuildRequires: libsidplayfp-devel >= 1.1.0

%description

%prep
%setup -q -n gstsidplayfp-%{version}

%build
%configure \
    --enable-debug --enable-gtk-doc \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR="%{buildroot}"

# Clean out files that should not be part of the rpm.
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la

%files
%doc AUTHORS COPYING README
%{_libdir}/gstreamer-%{majorminor}/libgstsidfp.so

%changelog
* Sat Feb 08 2014 Jari Karppinen <jari.p.karppinen@gmail.com> - 0.10.0-1
- Initial RPM packaging
