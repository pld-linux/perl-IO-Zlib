%include	/usr/lib/rpm/macros.perl
Summary:	IO-Zlib perl module
Summary(pl):	Modu³ perla IO-Zlib
Name:		perl-IO-Zlib
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-Zlib-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Compress-Zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO-Zlib perl module.

%description -l pl
Modu³ perla IO-Zlib.

%prep
%setup -q -n IO-Zlib-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/IO/Zlib.pm
%{_mandir}/man3/*
