#!/usr/bin/env bash
set -e

BASE="src/softadastra"

# Tous les dossiers à créer
MODULES=(
  algorithms containers core experimental io memory net
  concurrency chrono numeric iterator
)

for m in "${MODULES[@]}"; do
  mkdir -p "$BASE/$m"
  touch "$BASE/$m/__init__.py"
done

# Fichiers spécifiques de base
touch "$BASE/py.typed"                   # pour le typage PEP 561
touch "$BASE/__init__.py"                # import public
touch "$BASE/core/types.py"
touch "$BASE/core/errors.py"
touch "$BASE/core/utils.py"
touch "$BASE/core/config.py"

touch "$BASE/algorithms/sorting.py"
touch "$BASE/algorithms/searching.py"
touch "$BASE/algorithms/numeric.py"
touch "$BASE/algorithms/functional.py"

touch "$BASE/containers/vector.py"
touch "$BASE/containers/deque.py"
touch "$BASE/containers/map.py"
touch "$BASE/containers/set.py"
touch "$BASE/containers/queue.py"
touch "$BASE/containers/priority_queue.py"

touch "$BASE/io/filesystem.py"
touch "$BASE/io/text.py"
touch "$BASE/io/network.py"

touch "$BASE/memory/smart_pointer.py"
touch "$BASE/memory/allocator.py"

touch "$BASE/net/client.py"
touch "$BASE/net/auth.py"
touch "$BASE/net/endpoints.py"

touch "$BASE/concurrency/threading.py"
touch "$BASE/concurrency/async_utils.py"
touch "$BASE/concurrency/locks.py"

touch "$BASE/chrono/time_utils.py"

touch "$BASE/numeric/math_ext.py"
touch "$BASE/numeric/statistics.py"
touch "$BASE/numeric/random_ext.py"

touch "$BASE/iterator/itertools_ext.py"
touch "$BASE/iterator/range_adaptor.py"

echo "✅ Structure Softadastra créée."
