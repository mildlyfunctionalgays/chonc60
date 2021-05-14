with import <nixpkgs> { };

let
  python = python3;
  pythonPackages = python.pkgs;
  toPythonModule = drv:
    drv.overrideAttrs (oldAttrs: {
      # Use passthru in order to prevent rebuilds when possible.
      passthru = (oldAttrs.passthru or { }) // {
        pythonModule = python;
        pythonPath = [ ]; # Deprecated, for compatibility.
        requiredPythonModules = requiredPythonModules drv.propagatedBuildInputs;
      };
    });

in
mkShell rec {
  name = "kicad-env";
  buildInputs = [
    python3
    python3Packages.ipython
    (toPythonModule (pkgs.kicad-unstable.override { python3 = python3; }).src)
  ];
}
