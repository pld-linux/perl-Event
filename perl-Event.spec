#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event
Summary:	Event - a generic Perl event loop
Summary(pl):	Event - ogólna pêtla zdarzeñ dla Perla
Name:		perl-Event
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	ba450e6afd232ee63ac32b7fcb90ae34
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Event extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl
Rozszerzenie Event ma na celu udostêpnienie szerokiej klasie aplikacji
prostej i zoptymalizowanej pêtli zdarzeñ.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog README TODO

%{perl_vendorarch}/Event.pm
%{perl_vendorarch}/Event
%dir %{perl_vendorarch}/auto/Event
%{perl_vendorarch}/auto/Event/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Event/*.so
%{_mandir}/man3/*
