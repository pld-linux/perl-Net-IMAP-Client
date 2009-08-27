#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IMAP-Client
Summary:	Net::IMAP::Client - Not so simple IMAP client library
Summary(pl.UTF-8):	Net::IMAP::Client - Nie tak prosta biblioteka kliencka protokołu IMAP
Name:		perl-Net-IMAP-Client
Version:	0.93
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ebf441fc74abd4ed95446e7de4b4dcd9
URL:		http://search.cpan.org/dist/Net-IMAP-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-List-MoreUtils
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IMAP::Client provides methods to access an IMAP server. It aims
to provide a simple and clean API, while employing a rigorous parser
for IMAP responses in order to create Perl data structures from them.
The code is simple, clean and extensible.

%description -l pl.UTF-8
Net::IMAP::Client dostarcza metody dostępu do serwerów IMAP. Zamiarem
biblioteki jest zapewnić proste API.

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
%doc Changes README
%{perl_vendorlib}/Net/IMAP/*.pm
%{perl_vendorlib}/Net/IMAP/Client
%{_mandir}/man3/*
