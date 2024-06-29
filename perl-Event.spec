#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Event
%define		pnam	Event
Summary:	Event - a generic Perl event loop
Summary(pl.UTF-8):	Event - ogólna pętla zdarzeń dla Perla
Name:		perl-Event
Version:	1.28
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Event/%{pnam}-%{version}.tar.gz
# Source0-md5:	c40b79af3fec249ae1023dfc4213b375
URL:		https://metacpan.org/dist/Event
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Event extension aims to provide an simple and optimized event loop
for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie Event ma na celu udostępnienie szerokiej klasie aplikacji
prostej i zoptymalizowanej pętli zdarzeń.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Event.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README TODO
%{perl_vendorarch}/Event.pm
%{perl_vendorarch}/Event
%dir %{perl_vendorarch}/auto/Event
%attr(755,root,root) %{perl_vendorarch}/auto/Event/Event.so
%{_mandir}/man3/Event*.3pm*
