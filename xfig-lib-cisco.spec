Summary:	Network topology icons
Name:		xfig-lib-cisco
Version:	0.1
Release:	1
License:	no restrictions
Group:		X11/Applications/Graphics
Source0:	http://www.cisco.com/warp/public/503/3015_eps.zip
# Source0-md5:	af19cabebe528494202e7a34bf9ba616
URL:		http://www.cisco.com/warp/public/503/2.html
BuildRequires:	pstoedit
BuildRequires:	unzip
BuildArch:	noarch
Requires:	xfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Network topology icons from CISCO.

DISCLAIMER: Cisco Systems Inc. retains no copyrights or registration
to use these icons. Cisco icons are globally recognized and accepted
as the standard in network icon topologies. Use them freely without
alteration.

%prep
%setup -q -c

%build
for f in *.ps; do
	newf=$(echo "$f" | sed -e 's#\.ps#.fig#g')
	pstoedit -f fig "$f" "$newf"
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xfig/Libraries/Networks/Cisco

install *.fig $RPM_BUILD_ROOT%{_datadir}/xfig/Libraries/Networks/Cisco

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xfig/Libraries/Networks/Cisco
