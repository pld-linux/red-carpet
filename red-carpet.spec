%define		snap	20030914

Summary:	Software update utility and manager
Summary(pl):	Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem
Name:		red-carpet
Version:	2.0.3
Release:	%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	715a37461a862c72179001690f9884fe
Patch0:		%{name}-python-version.patch
Patch1:		%{name}-desktop.patch
URL:		http://ximian.com/apps/redcarpet.php3
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	scrollkeeper >= 0.3.12
BuildRequires:	libxslt-devel >= 1.0.30
Requires:	python-pygtk-gtk >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Software update utility and manager

%description -l pl
Narzêdzie do aktualizacji i zarz±dzania oprogramowaniem

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
glib-gettextize
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
%doc AUTHORS ChangeLog NEWS README HACKING
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/red_extra/*
%{_pixmapsdir}/%{name}/*
%{_pixmapsdir}/*.png
%{_datadir}/%{name}/*
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
