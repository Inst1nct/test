/^BSS/ {
    mac = gensub ( /^BSS[[:space:]]*([0-9a-fA-F:]+).*?$/, "\\1", "g", $0 );
}
/^[[:space:]]*SSID:/ {
    ssid = gensub ( /^[[:space:]]*SSID:[[:space:]]*([^\n]*).*?$/, "\\1", "g", $0 );
    printf ( "%s %s\n", mac, ssid );
}
