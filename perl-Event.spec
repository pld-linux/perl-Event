%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event
Summary:	Event - A Generic Perl Event Loop
Summary(cs):	Modul Event pro Perl
Summary(da):	Perlmodul Event
Summary(de):	Event Perl Modul
Summary(es):	M�dulo de Perl Event
Summary(fr):	Module Perl Event
Summary(it):	Modulo di Perl Event
Summary(ja):	Event Perl �⥸�塼��
Summary(ko):	Event �� ����
Summary(no):	Perlmodul Event
Summary(pl):	Modu� Perla Event
Summary(pt):	M�dulo de Perl Event
Summary(pt_BR):	M�dulo Perl Event
Summary(ru):	������ ��� Perl Event
Summary(sv):	Event Perlmodul
Summary(uk):	������ ��� Perl Event
Summary(zh_CN):	Event Perl ģ��
Name:		perl-Event
Version:	0.87
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	1c95b43cedb6f677e585d03b55010d20
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Event - This extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l cs
Modul Event pro Perl.

%description -l da
Perlmodul Event.

%description -l de
Event Perl Modul.

%description -l es
M�dulo de Perl Event.

%description -l fr
Module Perl Event.

%description -l it
Modulo di Perl Event.

%description -l ja
Event Perl �⥸�塼��

%description -l ko
Event �� ����.

%description -l no
Perlmodul Event.

%description -l pl
Event - rozszerzenie to ma na celu udost�pnienie szerokiej klasie
aplikacji prostej i zoptymalizowanej p�tli zdarze�.

%description -l pt
M�dulo de Perl Event.

%description -l pt_BR
M�dulo Perl Event.

%description -l ru
������ ��� Perl Event.

%description -l sv
Event Perlmodul.

%description -l uk
������ ��� Perl Event.

%description -l zh_CN
Event Perl ģ��

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
