Summary:	Software update utility and manager
Summary(pl):	Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem
Name:		red-carpet
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.ximian.com:/pub/red-carpet/source/%{name}-%{version}.tar.gz
URL:		http://ximian.com/apps/redcarpet.php3
BuildRequires:	gnome-libs-devel >= 1.0.54
BuildRequires:	gtkhtml-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libglade
BuildRequires:	gnome-print-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	popt-devel
BuildRequires:	libxml-devel
BuildRequires:	gnet-devel >= 1.0.4
BuildRequires:	gal-devel
BuildRequires:	rpm-devel >= 4.0
BuildRequires:	db3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Software update utility and manager

%description -l pl
Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem

%prep
%setup -q

%build
RPM_PREFIX=/usr; export RPM_PREFIX
%configure \
	--with-rpm-prefix \
	--enable-backend-rpm4=yes \
	--enable-console-helper=yes \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
!!FIXME!!
%{_pixmapsdir}/*
