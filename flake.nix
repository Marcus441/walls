{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin"];

    forAllSystems = nixpkgs.lib.genAttrs supportedSystems;

    importPkgs = system: import nixpkgs {inherit system;};
  in {
    devShells = forAllSystems (system: let
      pkgs = importPkgs system;
    in {
      default = pkgs.mkShellNoCC {
        packages = with pkgs; [
          poetry
        ];
      };
    });
  };
}
