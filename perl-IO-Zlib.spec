%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Zlib
Summary:	IO::Zlib Perl module - IO:: style interface to Compress::Zlib
Summary(pl):	Modu� Perla IO::Zlib - interfejs w stylu IO:: do modu�u Compress::Zlib
Name:		perl-IO-Zlib
Version:	1.01
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Compress-Zlib
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%description -l pl
Modu� IO::Zlib udost�pnia interfejs w stylu IO:: do modu�u
Compress::Zlib, a w ten spos�b do plik�w skompresowanych gzipem lub
bibliotek� zlib. Udost�pnia wiele metod takich samych jak interfejs
IO::Handle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/IO/Zlib.pm
%{_mandir}/man3/*
