# Botanik roadmap

Goal: board game → digital. A pure rules engine that powers three things:
1. **The talk (9 Dec):** game design, how to encode the rules, trade-offs, and turning the game into a simulation model to find the best strategy.
2. **Monte Carlo simulations:** players playing many games against each other.
3. **A playable prototype:** friends play via a shared link.

## Architecture principle

The engine is pure: no UI code and no hidden randomness inside it. Sims and UI both sit on top of the same API:

- `GameState`
- `legal_moves(state)`
- `apply_move(state, move)` → new state
- `is_over(state)`, `score(state)`

## Steps

### 1. Finish the `Column` refactor
- [ ] Pick one representation for `players_tiles` (dict + MappingProxyType / tuple / frozenset)
- [ ] Make `__post_init__`, `new()`, `get_player_tile`, `update_player_tile` all agree with it
- [ ] Decide whether `Column`/`Board`/`Machine` need to be hashable (needed for sets, dict keys, caching states in sims)
- [ ] Apply the same choice to `Machine` for consistency
- [ ] Clarify the meca botanist rule, then revisit `swap_central_tile_with_meca_botanist` (return the removed tile? is "swap" the right name?)
- [ ] Add tests for `get_player_tile` and `update_player_tile`

### 2. Fix the tests
- [ ] Replace `try/except` with `pytest.raises` (some tests currently pass without the error ever being raised, e.g. `test_invalid_column`, `test_invalid_source_tile`)
- [ ] Update stale expectations (list vs tuple, old `dict_keys` message, `AllTiles` tests with 1–2 tiles)

### 3. Load the real tile set
- [ ] Build `AllTiles` from `docs/botanik-tiles.csv`
- [ ] Fix the name mismatch: CSV `meca-botanist` vs enum `meca_botanist`
- [ ] Fix the `AllTiles` uniqueness check: `(color, type, flowers)` is not unique in the real set (e.g. two blue corners with 0 flowers)
- [ ] Shuffled draw stack

### 4. Game loop
- [ ] `GameState` (board, both machines, draw stack, current player)
- [ ] Setup (deal the starting central tiles)
- [ ] `legal_moves`
- [ ] `apply_move`
- [ ] End-of-game check and scoring
- [ ] Random player, then random-vs-random full game

### 5. Simulations
- [ ] Run many games, collect results
- [ ] Compare strategies

### 6. Prototype UI
- [ ] Decide: hotseat (one screen, simpler) first, online (server holds state, syncs players) later
- [ ] FastAPI backend wrapping the engine + simple frontend
- [ ] Shareable link

## Talk material
Keep `docs/decisions.md` up to date as you go: the choice, the alternatives, why.
