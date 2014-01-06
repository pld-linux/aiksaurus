#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	An English-language thesaurus library
Summary(pl.UTF-8):	Angielskojęzyczna biblioteka słownika wyrazów bliskoznacznych
Name:		aiksaurus
Version:	1.2.1
Release:	16
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/aiksaurus/%{name}-%{version}.tar.gz
# Source0-md5:	3eae03b7c49843ccc9262e52846ea6b4
Patch0:		%{name}-pkgconfig.patch
Patch1:		%{name}-configure_fix.patch
Patch2:		%{name}-gcc43.patch
Patch3:		format_security.patch
URL:		http://aiksaurus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Obsoletes:	Aiksaurus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities. A basic command line
thesaurus program is also included.

%description -l pl.UTF-8
Angielskojęzyczna biblioteka słownika wyrazów bliskoznacznych, która
może być stosowana w procesorach tekstu, klientach pocztowych i innym
oprogramowaniu. Prosty program działający z linii poleceń również
został dołączony.

%package devel
Summary:	Header files for Aiksaurus
Summary(pl.UTF-8):	Pliki nagłówkowe Aiksaurus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	Aiksaurus-devel

%description devel
The header files are only needed for development of programs using the
Aiksaurus.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek Aiksaurus.

%package static
Summary:	Static Aiksaurus library
Summary(pl.UTF-8):	Biblioteka statyczna Aiksaurus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	Aiksaurus-static

%description static
Static Aiksaurus library.

%description static -l pl.UTF-8
Biblioteka statyczna Aiksaurus.

%package gtk
Summary:	GTK+ frontend for Aiksaurus, an English thesaurus
Summary(pl.UTF-8):	Frontend GTK+ dla Aiksaurusa - angielskojęzycznego słownika wyrazów bliskoznacznych
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.0.0

%description gtk
GTK+ frontend for Aiksaurus, an English thesaurus.

%description gtk -l pl.UTF-8
Frontend GTK+ dla Aiksaurusa - angielskojęzycznego słownika wyrazów
bliskoznacznych.

%package gtk-devel
Summary:	Header files for GTK+ frontend for Aiksaurus
Summary(pl.UTF-8):	Pliki nagłówkowe frontendu GTK+ dla Aiksaurusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.0.0

%description gtk-devel
Header files for GTK+ frontend for Aiksaurus.

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe frontendu GTK+ dla Aiksaurusa.

%package gtk-static
Summary:	Static version of GTK+ frontend for Aiksaurus
Summary(pl.UTF-8):	Statycza wersja frontendu GTK+ dla Aiksaurusa
Group:		Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static version of GTK+ frontend for Aiksaurus.

%description gtk-static -l pl.UTF-8
Statycza wersja frontendu GTK+ dla Aiksaurusa.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
#LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libAiksaurus*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README base/CHANGES
%attr(755,root,root) %{_bindir}/aiksaurus
%attr(755,root,root) %{_bindir}/caiksaurus
%attr(755,root,root) %{_libdir}/libAiksaurus-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAiksaurus-*.so.?
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAiksaurus.so
%{_includedir}/Aiksaurus
%exclude %{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_pkgconfigdir}/aiksaurus-*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libAiksaurus.a
%endif

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaiksaurus
%attr(755,root,root) %{_libdir}/libAiksaurusGTK-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libAiksaurusGTK-*.so.?

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAiksaurusGTK.so
%{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_pkgconfigdir}/gaiksaurus-*.pc

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libAiksaurusGTK.a
%endif
