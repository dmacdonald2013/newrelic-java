Summary: New Relic Java Agent Release
Name: newrelic-java
Version: %{version}
Release: 1
License: Proprietary
BuildArch: noarch
Source0: newrelic-java-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
NewRelic Java Agent

%prep

%setup -c -T
unzip %{SOURCE0}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/newrelic
mkdir -p %{buildroot}/opt/newrelic/newrelic-%{version}

cp -rp newrelic/* %{buildroot}/opt/newrelic/newrelic-%{version}
cp -rp newrelic/newrelic.yml %{buildroot}/etc/newrelic

ln -F -s newrelic-%{version}/newrelic.jar %{buildroot}/opt/newrelic/newrelic.jar

%files
%defattr(0644,root,root,0755)
/opt/newrelic/newrelic-%{version}/
/opt/newrelic/newrelic.jar

%defattr(0644,root,root,0755)
%config(noreplace) /etc/newrelic
