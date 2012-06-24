%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	IO-Zlib perl module
Summary(pl):	Modu� perla IO-Zlib
Name:		perl-IO-Zlib
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-Zlib-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-Compress-Zlib
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Compress-Zlib
BuildRoot:	/tmp/%{name}-%{version}-root

%description
IO-Zlib perl module.

%description -l pl
Modu� perla IO-Zlib.

%prep
%setup -q -n IO-Zlib-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IO/Zlib
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/IO/Zlib.pm
%{perl_sitearch}/auto/IO/Zlib

%{_mandir}/man3/*
