Summary:	An English-language thesaurus library
Summary(pl):	Angielskojêzyczna biblioteka s³ownika wyrazów bliskoznacznych
Name:		aiksaurus
Version:	1.0.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/aiksaurus/%{name}-%{version}.tar.gz
# Source0-md5:	43892e723bdc516516af69b16489f8cf
URL:		http://aiksaurus.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Obsoletes:	Aiksaurus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities. A basic command line
thesaurus program is also included.

%description -l pl
Angielskojêzyczna biblioteka s³ownika wyrazów bliskoznacznych, która
mo¿e byæ stosowana w procesorach tekstu, klientach pocztowych i innym
oprogramowaniu. Prosty program dzia³aj±cy z linii poleceñ równie¿
zosta³ do³±czony.

%package devel
Summary:	Header files for Aiksaurus
Summary(pl):	Pliki nag³ówkowe Aiksaurus
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel
Obsoletes:	Aiksaurus-devel

%description devel
The header files are only needed for development of programs using the
Aiksaurus.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych bibliotek Aiksaurus.

%package static
Summary:	Static Aiksaurus library
Summary(pl):	Biblioteka statyczna Aiksaurus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	Aiksaurus-static

%description static
Static Aiksaurus library.

%description static -l pl
Biblioteka statyczna Aiksaurus.

%package gtk
Summary:	GTK+ frontend for Aiksaurus, an English thesaurus
Summary(pl):	Frontend GTK+ dla Aiksaurusa - angielskojêzycznego s³ownika wyrazów bliskoznacznych
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2 >= 2.0.0

%description gtk
GTK+ frontend for Aiksaurus, an English thesaurus.

%description gtk -l pl
Frontend GTK+ dla Aiksaurusa - angielskojêzycznego s³ownika wyrazów
bliskoznacznych.

%package gtk-devel
Summary:	Header files for GTK+ frontend for Aiksaurus
Summary(pl):	Pliki nag³ówkowe frontendu GTK+ dla Aiksaurusa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	%{name}-gtk = %{version}
Requires:	gtk+2-devel >= 2.0.0

%description gtk-devel
Header files for GTK+ frontend for Aiksaurus.

%description gtk-devel -l pl
Pliki nag³ówkowe frontendu GTK+ dla Aiksaurusa.

%package gtk-static
Summary:	Static version of GTK+ frontend for Aiksaurus
Summary(pl):	Statycza wersja frontendu GTK+ dla Aiksaurusa
Group:		Development/Libraries
Requires:	%{name}-gtk-devel = %{version}

%description gtk-static
Static version of GTK+ frontend for Aiksaurus.

%description gtk-static -l pl
Statycza wersja frontendu GTK+ dla Aiksaurusa.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAiksaurus.so
%{_libdir}/libAiksaurus.la
%{_includedir}/Aiksaurus
%exclude %{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_pkgconfigdir}/aiksaurus-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libAiksaurus.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaiksaurus
%attr(755,root,root) %{_libdir}/libAiksaurusGTK-*.so.*.*.*

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAiksaurusGTK.so
%{_libdir}/libAiksaurusGTK.la
%{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_pkgconfigdir}/gaiksaurus-*.pc

%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libAiksaurusGTK.a
