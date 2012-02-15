# Generated from thin-1.3.1.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	thin

Summary:	A thin and fast web server
Name:		rubygem-%{rbname}

Version:	1.3.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://code.macournoyer.com/thin/
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)

%description
A thin and fast web server

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/thin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack/adapter
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/backends
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers
%dir %{ruby_sitearchdir}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/backends/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers/*.erb
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/%{rbname}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack/adapter/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/*.erb
%{ruby_sitearchdir}/thin_parser.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
