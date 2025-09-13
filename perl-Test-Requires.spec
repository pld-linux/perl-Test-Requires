#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	Requires
Summary:	Test::Requires - checks to see if the module can be loaded
Summary(pl.UTF-8):	Test::Requires - sprawdzanie, czy moduł może być załadowany
Name:		perl-Test-Requires
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	999d6c4e46ea7baae7a5113292e02ed8
URL:		https://metacpan.org/dist/Test-Requires
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.61}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Requires checks to see if the module can be loaded.

If this fails rather than failing tests this skips all tests.

%description -l pl.UTF-8
Test::Requires sprawdza, czy moduł może być załadowany.

Jeśli to nie powiedzie się, to zamiast niepowodzeń przy uruchamianiu
testów pomijane są wszystkie testy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Requires.pm
%{_mandir}/man3/Test::Requires.3pm*
