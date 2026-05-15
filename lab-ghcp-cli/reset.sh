#!/bin/bash
# Resets GitHub Copilot CLI lab to its original state.
# Called by reset-all.sh on codespace reload.

echo "🔄 Resetting GitHub Copilot CLI lab..."
git checkout -- lab-ghcp-cli/
git clean -fd lab-ghcp-cli/
echo "✅ GitHub Copilot CLI lab ready!"
