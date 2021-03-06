#!/bin/bash

pushd `dirname ${BASH_SOURCE[0]}` >/dev/null
OSSIMRPM_SCRIPT_DIR=$PWD
popd > /dev/null

pushd $OSSIMRPM_SCRIPT_DIR/../.. > /dev/null
export OSSIM_DEV_HOME=$PWD
export OSSIM_INSTAL_PREFIX=$OSSIM_DEV_HOME/install

mkdir -p $OSSIM_DEV_HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Unable to create rpmbuild directories."
  exit 1
fi
pushd $OSSIM_DEV_HOME/rpmbuild/SOURCES >/dev/null
#wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/opencv-3.3.0.tar.gz -O opencv-3.3.0.tar.gz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/ffmpeg-4.1.1.tar.bz2 -O ffmpeg-4.1.1.tar.bz2
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/x264-0.155-20180923-545de2f.tgz -O x264-0.155-20180923-545de2f.tgz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/aws-sdk-cpp-1.0.62.tar.gz -O 1.0.62.tar.gz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/OpenSceneGraph-3.6.2.zip -O OpenSceneGraph-3.6.2.zip
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/0001-Cmake-fixes.patch -O 0001-Cmake-fixes.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/0001-Update-Aether-to-0.9.0.M3.patch -O 0001-Update-Aether-to-0.9.0.M3.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/0002-Fix-invalid-char.patch -O 0002-Fix-invalid-char.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/0003-Activate-osgviewerWX.patch -O 0003-Activate-osgviewerWX.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/0005-Use-generics-in-modello-generated-code.patch -O 0005-Use-generics-in-modello-generated-code.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/szip-2.1.tar.gz -O szip-2.1.tar.gz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/szip-linking.patch -O szip-linking.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/szip-opt.patch -O szip-opt.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/libjpeg12-turbo-1.4.2.tar.gz -O libjpeg12-turbo-1.4.2.tar.gz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/libjpeg12-turbo14-noinst.patch -O libjpeg12-turbo14-noinst.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/libjpeg12-turbo-header-files.patch -O libjpeg12-turbo-header-files.patch
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/gpstk-2.3.src.tar.gz -O gpstk-2.3.src.tar.gz
wget -q https://s3.amazonaws.com/ossimlabs/dependencies/source/hdf5a-1.8.17.tar.gz -O hdf5a-1.8.17.tar.gz
popd >/dev/null

cp $OSSIMRPM_SCRIPT_DIR/../rpm_specs/*.spec $OSSIM_DEV_HOME/rpmbuild/SPECS/
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Unable to copy spec files from $OSSIMRPM_SCRIPT_DIR/../rpm_specs/*.spec to location $OSSIM_DEV_HOME/rpmbuild/SPECS."
  exit 1
fi


pushd ${OSSIM_DEV_HOME}/rpmbuild/SOURCES
  export OPENCV_VERSION=3.3.0
  wget https://s3.amazonaws.com/ossimlabs/dependencies/source/opencv-${OPENCV_VERSION}.tar.gz
  tar xvf opencv-${OPENCV_VERSION}.tar.gz
  pushd opencv-${OPENCV_VERSION} >/dev/null
  find ./ -iname "len*.*" -exec rm {} \;
  # rm -rf modules/xfeatures2d/
  popd > /dev/null; tar zcf opencv-clean-${OPENCV_VERSION}.tar.gz opencv-${OPENCV_VERSION}/
  wget https://s3.amazonaws.com/ossimlabs/dependencies/source/opencv_contrib-${OPENCV_VERSION}.tar.gz -O opencv_contrib-clean-${OPENCV_VERSION}.tar.gz
  # tar xvf opencv_contrib-${OPENCV_VERSION}.tar.gz
  # pushd opencv_contrib-${OPENCV_VERSION}
  # rm -rf modules/xfeatures2d/
  # popd >/dev/null; tar zcf opencv_contrib-clean-${OPENCV_VERSION}.tar.gz opencv_contrib-${OPENCV_VERSION}/
popd > /dev/null

#rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "_smp_mflags -j4" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/opencv.spec
#if [ $? -ne 0 ]; then
#  echo; echo "ERROR: Build failed for opencv 3.3.0 rpm build."
#  exit 1
#fi


rpmbuild -ba --define "_without_asm 1" --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/x264.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for x264 rpm build."
  exit 1
fi


rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/ffmpeg.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for ffmpeg rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/aws-sdk-cpp.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for aws-sdk-cpp rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/hdf5a.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for hdf5a rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/libjpeg12-turbo.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for libjpeg12-turbo rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/gpstk.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for gpstk rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 3" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/szip.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for szip rpm build."
  exit 1
fi

rpmbuild -ba --define "_topdir ${OSSIM_DEV_HOME}/rpmbuild" --define "BUILD_RELEASE 1" ${OSSIM_DEV_HOME}/rpmbuild/SPECS/OpenSceneGraph.spec
if [ $? -ne 0 ]; then
  echo; echo "ERROR: Build failed for OpenSceneGraph rpm build."
  exit 1
fi

getOsInfo os major_version minor_version os_arch

rpmdir=${OSSIM_DEV_HOME}/dependency-rpms
if [ -d "$rpmdir" ] ; then
  rm -rf $rpmdir/*
fi
mkdir -p $rpmdir

pushd ${OSSIM_DEV_HOME}/rpmbuild/RPMS >/dev/null
  mv `find ./${os_arch} -name "*.rpm"` $rpmdir/
popd > /dev/null

pushd ${OSSIM_DEV_HOME} >/dev/null
tar cvfz dependency-rpms.tgz dependency-rpms
popd > /dev/null
