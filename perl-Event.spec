%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event
Summary:	Event - A Generic Perl Event Loop
Summary(cs):	Modul Event pro Perl
Summary(da):	Perlmodul Event
Summary(de):	Event Perl Modul
Summary(es):	Módulo de Perl Event
Summary(fr):	Module Perl Event
Summary(it):	Modulo di Perl Event
Summary(ja):	Event Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Event ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Event
Summary(pl):	Modu³ Perla Event
Summary(pt):	Módulo de Perl Event
Summary(pt_BR):	Módulo Perl Event
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Event
Summary(sv):	Event Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Event
Summary(zh_CN):	Event Perl Ä£¿é
Name:		perl-Event
Version:	0.87
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
Módulo de Perl Event.

%description -l fr
Module Perl Event.

%description -l it
Modulo di Perl Event.

%description -l ja
Event Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Event ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Event.

%description -l pl
Event - rozszerzenie to ma na celu udostêpnienie szerokiej klasie
aplikacji prostej i zoptymalizowanej pêtli zdarzeñ.

%description -l pt
Módulo de Perl Event.

%description -l pt_BR
Módulo Perl Event.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Event.

%description -l sv
Event Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Event.

%description -l zh_CN
Event Perl Ä£¿é

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
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

%{perl_sitearch}/Event.pm
%{perl_sitearch}/Event
%dir %{perl_sitearch}/auto/Event
%{perl_sitearch}/auto/Event/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Event/*.so
%{_mandir}/man3/*
