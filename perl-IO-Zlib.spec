%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Zlib
Summary:	IO::Zlib Perl module - IO:: style interface to Compress::Zlib
Summary(pl):	Modu³ Perla IO::Zlib - interfejs w stylu IO:: do modu³u Compress::Zlib
Name:		perl-IO-Zlib
Version:	1.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	914af0c54586d9e979fe03e5f1e341f0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Compress-Zlib
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%description -l pl
Modu³ IO::Zlib udostêpnia interfejs w stylu IO:: do modu³u
Compress::Zlib, a w ten sposób do plików skompresowanych gzipem lub
bibliotek± zlib. Udostêpnia wiele metod takich samych jak interfejs
IO::Handle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/IO/Zlib.pm
%{_mandir}/man3/*
