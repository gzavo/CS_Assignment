{
  description = "Flake used for computational science.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      nixpkgs.overlays = [
        (self: super: {
          python312Packages = super.python312Packages.override {
            overrides = pyself: pysuper: {
              lmfit = pysuper.lmfit.overrideAttrs {doCheck = false;};
            };
          };
          # (nfinal: nprev: {
          #   lmfit = nprev.lmfit.overridePythonAttrs (oldAttrs: { doCheck = false; doInstallCheck = false; });
          # })
          # = super.python312.override {
          # packageOverrides = pyfinal: pyprev: {
          # lmfit = pyprev.lmfit.overrideAttrs {
          # doCheck = false;
          # };
          # };
          # };
        }
        )
      ];

      devShells.${system}.default = pkgs.mkShell {
        nativeBuildInputs = with pkgs; [
          python312Packages.python
          python312Packages.jupyter
          python312Packages.pandas
          python312Packages.polars
          python312Packages.matplotlib
          python312Packages.ipympl
          python312Packages.numpy
          python312Packages.alive-progress
          python312Packages.lmfit

          typst
        ];

      };

      doCheck = false;
    };
}
