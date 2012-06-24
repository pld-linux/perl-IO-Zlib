#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Zlib
Summary:	IO::Zlib Perl module - IO:: style interface to Compress::Zlib
Summary(pl):	Modu� Perla IO::Zlib - interfejs w stylu IO:: do modu�u Compress::Zlib
Name:		perl-IO-Zlib
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	010c1b3431a7892d1f8f17f17ac49669
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/IO/Zlib.pm
%{_mandir}/man3/*
