FROM ubuntu:focal
SHELL ["/bin/bash", "-c"]
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y \
    software-properties-common \
    build-essential \
    python3-pip \
    gfortran \
    libnetcdf-dev \
    libnetcdff-dev \
    netcdf-bin \
    nco \
    git
RUN pip3 install \
    Cython \
    h5py \
    netCDF4 \
    pandas \
    cftime
ADD . .
RUN git clone https://github.com/cshields143/climate_indices.git
WORKDIR /climate_indices
RUN python3 setup.py install
WORKDIR /
CMD ./run
