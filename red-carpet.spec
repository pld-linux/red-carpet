Summary:	Software update utility and manager
Summary(pl):	Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem
Name:		red-carpet
Version:	2.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d67e8e355070ded001b0f2984efd8b28
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
URL:		http://ximian.com/apps/redcarpet.php3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.0.30
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	scrollkeeper >= 0.3.12
Requires:	python-pygtk-gtk >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software update utility and manager.

%description -l pl
Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
glib-gettextize -f
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure 
#	--enable-standalone

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/red_extra
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
%{_datadir}/%{name}
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
