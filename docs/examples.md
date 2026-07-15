# Examples

```bash
uv run release-passport import tests/fixtures/passport-import
uv run release-passport diff tests/fixtures/passport-diff/old.json tests/fixtures/passport-diff/new.json
uv run release-passport verify tests/fixtures/passport-signing/signed-passport.json
```

The shipped fixture includes an Argo CD application revision change, manifest checksum, image digests, and changed Kubernetes resources.
