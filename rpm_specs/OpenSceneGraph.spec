#
# Copyright (c) 2005 - 2014 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%define apivers 3.6.2
%define srcvers 3.6.2

Name:           OpenSceneGraph
Version:        %{apivers}
Release:        1%{?dist}
Summary:        High performance real-time graphics toolkit

Group:          Applications/Multimedia
# The OSGPL is just the wxWidgets license.
License:        wxWidgets
URL:            http://www.openscenegraph.org/
# Announced as stable, but published under developer_releases ;)
Source0:        http://www.openscenegraph.org/downloads/developer_releases/OpenSceneGraph-%{srcvers}.zip

Patch1:         0001-Cmake-fixes.patch
Patch2:         0002-Fix-invalid-char.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch3:         0003-Activate-osgviewerWX.patch

BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
# BuildRequires:  Inventor-devel
BuildRequires:  freeglut-devel
BuildRequires:  libgta-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libungif-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  doxygen graphviz
BuildRequires:  cmake
#BuildRequires:  wxGTK-devel
BuildRequires:  curl-devel
BuildRequires:  libxml2-devel
# BuildRequires:  gtkglext-devel
BuildRequires:  librsvg2-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  openal-soft-devel

BuildRequires:  qt-devel
BuildRequires:  qtwebkit-devel

BuildRequires:  SDL-devel

BuildRequires:  fltk-devel

BuildRequires:  gnuplot

BuildRequires:  libvncserver-devel

# According to the FPG, this should be defined, but it's not.
%define _fontdir /usr/share/fonts

%description
The OpenSceneGraph is an OpenSource, cross platform graphics toolkit for the
development of high performance graphics applications such as flight
simulators, games, virtual reality and scientific visualization.
Based around the concept of a SceneGraph, it provides an object oriented
framework on top of OpenGL freeing the developer from implementing and
optimizing low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%prep
%setup -q -c
cd OpenSceneGraph-%{srcvers}

sed -i -e 's,\.:/usr/share/fonts/ttf:,.:%{_fontdir}:/usr/share/fonts/ttf:,' \
src/osgText/Font.cpp

iconv -f ISO-8859-1 -t utf-8 AUTHORS.txt > AUTHORS.txt~
mv AUTHORS.txt~ AUTHORS.txt
cd ..

%build
mkdir -p BUILD
pushd BUILD
CFLAGS="${RPM_OPT_FLAGS} -pthread"
CXXFLAGS="${RPM_OPT_FLAGS} -pthread -std=c++11"
%cmake \
   -DBUILD_OSG_EXAMPLES=OFF \
   -DBUILD_DOCUMENTATION=OFF \
   ../OpenSceneGraph-%{srcvers} -Wno-dev
make VERBOSE=1 %{?_smp_mflags}

#make doc_openscenegraph doc_openthreads
popd

%install
pushd BUILD
make install DESTDIR=${RPM_BUILD_ROOT}

# Supposed to take OpenSceneGraph data
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/OpenSceneGraph
popd


%files
%doc OpenSceneGraph-%{srcvers}/{AUTHORS,LICENSE,NEWS}.txt
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/osgfilecache
%{_bindir}/present3D

%package libs
Summary:        Runtime libraries for OpenSceneGraph
Group:          Applications/Multimedia

%description libs
Runtime libraries files for OpenSceneGraph.

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files libs
%{_libdir}/osgPlugins-%{apivers}
#%exclude %{_libdir}/osgPlugins-%{apivers}/osgdb_qfont.so
%{_libdir}/libosgAnimation.so.*
%{_libdir}/libosgDB.so.*
%{_libdir}/libosgFX.so.*
%{_libdir}/libosgGA.so.*
%{_libdir}/libosgManipulator.so.*
%{_libdir}/libosgParticle.so.*
%{_libdir}/libosgPresentation.so.*
%{_libdir}/libosgShadow.so.*
%{_libdir}/libosgSim.so.*
%{_libdir}/libosg.so.*
%{_libdir}/libosgTerrain.so.*
%{_libdir}/libosgText.so.*
%{_libdir}/libosgUtil.so.*
%{_libdir}/libosgViewer.so.*
%{_libdir}/libosgVolume.so.*
%{_libdir}/libosgWidget.so.*

%package devel
Summary:        Development files for OpenSceneGraph
Group:          Applications/Multimedia
Requires:       OpenSceneGraph-libs = %{version}-%{release}
Requires:       OpenThreads-devel

%description devel
Development files for OpenSceneGraph.

%files devel
%{_includedir}/osg/
%{_includedir}/osgAnimation/
%{_includedir}/osgDB/
%{_includedir}/osgFX/
%{_includedir}/osgGA/
%{_includedir}/osgManipulator/
%{_includedir}/osgParticle/
%{_includedir}/osgShadow/
%{_includedir}/osgSim/
%{_includedir}/osgTerrain/
%{_includedir}/osgText/
%{_includedir}/osgUI/
%{_includedir}/osgUtil/
%{_includedir}/osgViewer/
%{_includedir}/osgVolume/
%{_includedir}/osgWidget/
%{_includedir}/osgPresentation/
%{_libdir}/libosg.so
%{_libdir}/libosgAnimation.so
%{_libdir}/libosgDB.so
%{_libdir}/libosgFX.so
%{_libdir}/libosgGA.so
%{_libdir}/libosgManipulator.so
%{_libdir}/libosgParticle.so
%{_libdir}/libosgShadow.so
%{_libdir}/libosgSim.so
%{_libdir}/libosgTerrain.so
%{_libdir}/libosgText.so
%{_libdir}/libosgUI.so
%{_libdir}/libosgUtil.so
%{_libdir}/libosgViewer.so
%{_libdir}/libosgVolume.so
%{_libdir}/libosgWidget.so
%{_libdir}/libosgPresentation.so
%{_libdir}/pkgconfig/openscenegraph.pc
%{_libdir}/pkgconfig/openscenegraph-osg*.pc


#%package examples-SDL
#Summary:        OSG sample applications using SDL
#Group:          Applications/Multimedia

# %description examples-SDL
# OSG sample applications using SDL.

# %files examples-SDL
# %{_bindir}/osgviewerSDL

# %package examples-fltk
# Summary:        OSG sample applications using FLTK
# Group:          Applications/Multimedia

# %description examples-fltk
# OSG sample applications using FLTK.

# %files examples-fltk
# %{_bindir}/osgviewerFLTK

#%package examples-gtk
#Summary:        OSG sample applications using gtk
#Group:          Applications/Multimedia

#%description examples-gtk
#OSG sample applications using gtk

# %files examples-gtk
#%{_bindir}/osgviewerGTK

# %package qt
# Summary:        OSG Qt bindings
# Group:          Applications/Multimedia

# %description qt
# OSG Qt bindings.

# %files qt
# %{_libdir}/libosgQt.so.*
# %dir %{_libdir}/osgPlugins-%{apivers}
#%{_libdir}/osgPlugins-%{apivers}/osgdb_qfont.so

# %post qt -p /sbin/ldconfig

# %postun qt -p /sbin/ldconfig

# %package qt-devel
# Summary:        OSG Qt development files
# Group:          Applications/Multimedia
# Requires:       OpenSceneGraph-qt = %{version}-%{release}
# Requires:       OpenSceneGraph-devel = %{version}-%{release}
# Requires:       qt-devel

# %description qt-devel
# Development files for OSG Qt bindings.

# %files qt-devel
# %{_includedir}/osgQt
# %{_libdir}/libosgQt.so
# %{_libdir}/pkgconfig/openscenegraph-osgQt.pc


# %package examples-qt
# Summary:        OSG sample applications using qt
# Group:          Applications/Multimedia

# %description examples-qt
# OSG sample applications using qt

# %files examples-qt
# %{_bindir}/osgviewerQt
#%{_bindir}/osgQtBrowser
#%{_bindir}/osgQtWidgets

# OpenSceneGraph-examples
# %package examples
# Summary:        Sample applications for OpenSceneGraph
# Group:          Applications/Multimedia

# %description examples
# Sample applications for OpenSceneGraph

# %files examples
# %{_bindir}/osg2cpp
# %{_bindir}/osganalysis
# %{_bindir}/osganimate
# %{_bindir}/osganimationeasemotion
# %{_bindir}/osganimationhardware
# %{_bindir}/osganimationmakepath
# %{_bindir}/osganimationmorph
# %{_bindir}/osganimationnode
# %{_bindir}/osganimationskinning
# %{_bindir}/osganimationsolid
# %{_bindir}/osganimationtimeline
# %{_bindir}/osganimationviewer
# %{_bindir}/osgatomiccounter
# %{_bindir}/osgautocapture
# %{_bindir}/osgautotransform
# %{_bindir}/osgbillboard
# %{_bindir}/osgblendequation
# %{_bindir}/osgcallback
# %{_bindir}/osgcamera
# %{_bindir}/osgcatch
# %{_bindir}/osgclip
# %{_bindir}/osgcluster
# %{_bindir}/osgcompositeviewer
# %{_bindir}/osgcomputeshaders
# %{_bindir}/osgcopy
# %{_bindir}/osgcubemap
# %{_bindir}/osgdatabaserevisions
# %{_bindir}/osgdelaunay
# %{_bindir}/osgdepthpartition
# %{_bindir}/osgdepthpeeling
# %{_bindir}/osgdistortion
# %{_bindir}/osgdrawinstanced
# %{_bindir}/osgfadetext
# %{_bindir}/osgfont
# %{_bindir}/osgforest
# %{_bindir}/osgfpdepth
# %{_bindir}/osgframerenderer
# %{_bindir}/osgfxbrowser
# %{_bindir}/osggameoflife
# %{_bindir}/osggeometry
# %{_bindir}/osggeometryshaders
# %{_bindir}/osggpx
# %{_bindir}/osggraphicscost
# %{_bindir}/osghangglide
# %{_bindir}/osghud
# %{_bindir}/osgimagesequence
# %{_bindir}/osgimpostor
# %{_bindir}/osgintersection
# %{_bindir}/osgkdtree
# %{_bindir}/osgkeyboard
# %{_bindir}/osgkeyboardmouse
# %{_bindir}/osgkeystone
# %{_bindir}/osglauncher
# %{_bindir}/osglight
# %{_bindir}/osglightpoint
# %{_bindir}/osglogicop
# %{_bindir}/osglogo
# %{_bindir}/osgmanipulator
# %{_bindir}/osgmemorytest
# %{_bindir}/osgmotionblur
# %{_bindir}/osgmovie
# %{_bindir}/osgmultiplemovies
# %{_bindir}/osgmultiplerendertargets
# %{_bindir}/osgmultitexture
# %{_bindir}/osgmultitexturecontrol
# %{_bindir}/osgmultitouch
# %{_bindir}/osgmultiviewpaging
# %{_bindir}/osgoccluder
# %{_bindir}/osgocclusionquery
# %{_bindir}/osgoit
# %{_bindir}/osgoscdevice
# %{_bindir}/osgoutline
# %{_bindir}/osgpackeddepthstencil
# %{_bindir}/osgpagedlod
# %{_bindir}/osgparametric
# %{_bindir}/osgparticle
# %{_bindir}/osgparticleeffects
# %{_bindir}/osgparticleshader
# %{_bindir}/osgpdf
# %{_bindir}/osgphotoalbum
# %{_bindir}/osgpick
# %{_bindir}/osgplanets
# %{_bindir}/osgpoints
# %{_bindir}/osgpointsprite
# %{_bindir}/osgposter
# %{_bindir}/osgprecipitation
# %{_bindir}/osgprerender
# %{_bindir}/osgprerendercubemap
# %{_bindir}/osgqfont
# %{_bindir}/osgreflect
# %{_bindir}/osgrobot
# %{_bindir}/osgscalarbar
# %{_bindir}/osgscreencapture
# %{_bindir}/osgscribe
# %{_bindir}/osgsequence
# %{_bindir}/osgshadercomposition
# %{_bindir}/osgshadergen
# %{_bindir}/osgshaders
# %{_bindir}/osgshaderterrain
# %{_bindir}/osgshadow
# %{_bindir}/osgshape
# %{_bindir}/osgsharedarray
# %{_bindir}/osgsidebyside
# %{_bindir}/osgsimpleshaders
# %{_bindir}/osgsimplegl3
# %{_bindir}/osgsimplifier
# %{_bindir}/osgsimulation
# %{_bindir}/osgslice
# %{_bindir}/osgspacewarp
# %{_bindir}/osgspheresegment
# %{_bindir}/osgspotlight
# %{_bindir}/osgstereoimage
# %{_bindir}/osgstereomatch
# %{_bindir}/osgteapot
# %{_bindir}/osgterrain
# %{_bindir}/osgtessellate
# %{_bindir}/osgtessellationshaders
# %{_bindir}/osgtext
# %{_bindir}/osgtext3D
# %{_bindir}/osgtexture1D
# %{_bindir}/osgtexture2D
# %{_bindir}/osgtexture3D
# %{_bindir}/osgtexturecompression
# %{_bindir}/osgtexturerectangle
# %{_bindir}/osgthirdpersonview
# %{_bindir}/osgthreadedterrain
# %{_bindir}/osguniformbuffer
# %{_bindir}/osgunittests
# %{_bindir}/osguserdata
# %{_bindir}/osguserstats
# %{_bindir}/osgvertexattributes
# %{_bindir}/osgvertexprogram
# %{_bindir}/osgviewerGLUT
# #%{_bindir}/osgviewerGTK
# #%{_bindir}/osgviewerWX
# %{_bindir}/osgvirtualprogram
# %{_bindir}/osgvnc
# %{_bindir}/osgvolume
# %{_bindir}/osgwidgetaddremove
# %{_bindir}/osgwidgetbox
# %{_bindir}/osgwidgetcanvas
# %{_bindir}/osgwidgetframe
# %{_bindir}/osgwidgetinput
# %{_bindir}/osgwidgetlabel
# %{_bindir}/osgwidgetmenu
# %{_bindir}/osgwidgetmessagebox
# %{_bindir}/osgwidgetnotebook
# %{_bindir}/osgwidgetperformance
# %{_bindir}/osgwidgetscrolled
# %{_bindir}/osgwidgetshader
# %{_bindir}/osgwidgetstyled
# %{_bindir}/osgwidgettable
# %{_bindir}/osgwidgetwindow
# %{_bindir}/osgwindows

%{_datadir}/OpenSceneGraph

# OpenThreads
%package -n OpenThreads
Summary:        OpenThreads
Group:          Applications/Multimedia
License:        wxWidgets

%description -n OpenThreads
OpenThreads is intended to provide a minimal & complete Object-Oriented (OO)
thread interface for C++ programmers.  It is loosely modeled on the Java
thread API, and the POSIX Threads standards.  The architecture of the
library is designed around "swappable" thread models which are defined at
compile-time in a shared object library.

%post -n OpenThreads -p /sbin/ldconfig

%postun -n OpenThreads -p /sbin/ldconfig

%files -n OpenThreads
%doc OpenSceneGraph-%{srcvers}/{AUTHORS,LICENSE,NEWS}.txt
%{_libdir}/libOpenThreads.so.*

# OpenThreads-devel
%package -n OpenThreads-devel
Summary:        Devel files for OpenThreads
Group:          Applications/Multimedia
License:        wxWidgets
Requires:       OpenThreads = %{version}-%{release}
Requires:       pkgconfig

%description -n OpenThreads-devel
Development files for OpenThreads.

%files -n OpenThreads-devel
%{_libdir}/pkgconfig/openthreads.pc
%{_libdir}/libOpenThreads.so
%{_includedir}/OpenThreads

%changelog
