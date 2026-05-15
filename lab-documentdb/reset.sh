#!/bin/bash
# Resets DocumentDB lab to its original state.
# Called by reset-all.sh on codespace reload.

echo "🔄 Resetting DocumentDB lab..."
git checkout -- lab-documentdb/
git clean -fd lab-documentdb/
echo "✅ DocumentDB lab ready!"