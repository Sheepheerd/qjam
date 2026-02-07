FROM nixos/nix:latest

RUN echo "experimental-features = nix-command flakes" >> /etc/nix/nix.conf

WORKDIR /app

COPY flake.nix flake.lock ./

RUN nix develop

COPY . .

EXPOSE 8000

CMD ["nix", "develop", "--command", "fastapi", "dev", "backend", "--host", "0.0.0.0", "--port", "8000"]