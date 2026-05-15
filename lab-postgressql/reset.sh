#!/bin/bash
# Resets Semantic Search lab to its original state.
# Called by reset-all.sh on codespace reload.

echo "🔄 Resetting Semantic Search lab..."
git checkout -- lab-semantic-search/
git clean -fd lab-semantic-search/
echo "✅ Semantic Search lab ready!"