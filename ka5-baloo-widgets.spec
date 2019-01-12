%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		baloo-widgets
Summary:	Baloo widgets
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	95f539a2488016d517b3d05fc58f7b19
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-baloo-devel >= 5.43.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.43.0
BuildRequires:	kf5-kfilemetadata-devel >= 5.43.0
BuildRequires:	kf5-ki18n-devel >= 5.43.0
BuildRequires:	kf5-kio-devel >= 5.43.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Widgets for Baloo.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/baloo_filemetadata_temp_extractor
%attr(755,root,root) %ghost %{_libdir}/libKF5BalooWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5BalooWidgets.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/baloofilepropertiesplugin.so
%{_datadir}/kservices5/baloofilepropertiesplugin.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/BalooWidgets
%{_libdir}/cmake/KF5BalooWidgets
%attr(755,root,root) %{_libdir}/libKF5BalooWidgets.so
