# On NIX enabled systems, just run `nix-shell`
# See https://nixos.org/manual/nixpkgs/stable/#python

with import <nixpkgs> { };

let
  pythonPackages = python38Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";

  buildInputs = [
    pythonPackages.python

    pythonPackages.matplotlib
    pythonPackages.numpy
    pythonPackages.pandas
    pythonPackages.geopy
    pythonPackages.scipy
    pythonPackages.future
    pythonPackages.toml
    pythonPackages.scikitimage
    pythonPackages.opencv4
    pythonPackages.ipython
    pythonPackages.jupyter
    pythonPackages.grip # Preview Github flavoured markdown
    pythonPackages.black # Code formatter
    taglib
    openssl
    git
    libxml2
    libxslt
    libzip
    zlib
  ];

}

