#!/bin/bash
# Resets Semantic Search lab to its original state.
# Called by reset-all.sh on codespace reload.

echo "🔄 Resetting PostgreSQL lab..."
git checkout -- lab-postgressql/
git clean -fd lab-postgressql/
echo "✅ PostgreSQL lab ready!"