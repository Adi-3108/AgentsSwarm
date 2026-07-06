"""
Tests for backend/app/utils/hash_helper.py
"""

import pytest
from backend.app.utils.hash_helper import hash_string, verify_hash, hash_bytes


def test_sha256_hash_consistency():
    """Same input must produce same SHA-256 digest."""
    h1 = hash_string("hello world")
    h2 = hash_string("hello world")
    assert h1 == h2


def test_sha256_different_inputs():
    """Different inputs must produce different SHA-256 digests."""
    h1 = hash_string("hello")
    h2 = hash_string("world")
    assert h1 != h2


def test_blake2b_consistency():
    """Same input must produce same BLAKE2b digest."""
    h1 = hash_string("nexsus", algorithm="blake2b")
    h2 = hash_string("nexsus", algorithm="blake2b")
    assert h1 == h2


def test_verify_hash_success():
    """verify_hash must return True for matching hash."""
    digest = hash_string("secure-payload")
    assert verify_hash("secure-payload", digest) is True


def test_verify_hash_failure():
    """verify_hash must return False for non-matching hash."""
    assert verify_hash("wrong", "deadbeef" * 8) is False


def test_hash_bytes():
    """hash_bytes must return consistent hex digest."""
    data = b"binary data"
    h1 = hash_bytes(data)
    h2 = hash_bytes(data)
    assert h1 == h2
    assert len(h1) == 64  # SHA-256 produces 64-char hex
