# **walls**

A tiered wallpaper collection organized by resolution and category.

## **Usage**

### **Nix (Home Manager)**

Incorporate specific tiers into your configuration using fetchFromGitHub with
sparse checkout for efficiency:

```bash
{ pkgs }:  
let  
  walls = pkgs.fetchFromGitHub {  
    owner = "username";  
    repo = "walls";  
    rev = "commit-hash";  
    hash = ""; # hash goes here 
    sparseCheckout = [ "walled_tiers/4k/anime" ];  
  };  
in {  
  home.file."Pictures/wallpapers".source = "${walls}/walled_tiers/4k/anime";  
}
```

### **Git Sparse Checkout**

Clone specific tiers without downloading the entire repository:

```bash
git clone --filter=blob:none --sparse https://github.com/username/walls.git
cd walls
git sparse-checkout set walled_tiers/4k/minimal walled_tiers/8k
```

## **Structure**

Images are categorized by horizontal width:

- 8k: \>= 7680px
- 4k: \>= 3840px
- 1440p: \>= 2560px
- 1080p: \>= 1920px
- low\_res: \< 1920px

Development tools and sorting logic are located in the scripts/ directory.
