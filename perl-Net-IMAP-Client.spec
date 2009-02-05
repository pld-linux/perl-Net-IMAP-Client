#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IMAP-Client
Summary:	Net::IMAP::Client - Not so simple IMAP client library
#Summary(pl.UTF-8):	
Name:		perl-Net-IMAP-Client
Version:	0.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b974ece04e4196f3baa12c5518fc15bd
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
Net::IMAP::Client provides methods to access an IMAP server.  It aims
to provide a simple and clean API, while employing a rigorous parser
for IMAP responses in order to create Perl data structures from them.
The code is simple, clean and extensible.

# %description -l pl.UTF-8
# TODO

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
