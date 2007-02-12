#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event
Summary:	Event - a generic Perl event loop
Summary(pl.UTF-8):   Event - ogólna pętla zdarzeń dla Perla
Name:		perl-Event
Version:	1.06
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	789cc8f0b011653cac6451cfef3053a8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Event extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie Event ma na celu udostępnienie szerokiej klasie aplikacji
prostej i zoptymalizowanej pętli zdarzeń.

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
