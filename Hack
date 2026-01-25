#!/bin/bash
# LORD PREMO TikTok Hack Command

if [ -z "$1" ]; then
    echo "Usage: hack tiktok <target_name>"
    exit 1
fi

if [ "$1" = "tiktok" ]; then
    shift
    python ~/Tiktok-hack-/hack.py "$@"
else
    echo "Unknown option: $1"
    echo "Usage: hack tiktok <target_name>"
fi
