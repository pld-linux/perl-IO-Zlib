%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Zlib
Summary:	IO::Zlib - IO:: style interface to L<Compress::Zlib>
Name:		perl-IO-Zlib
Version:	1.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Compress-Zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<IO::Zlib> provides an IO:: style interface to L<Compress::Zlib>
and hence to gzip/zlib compressed files. It provides many of the same
methods as the L<IO::Handle> interface.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
