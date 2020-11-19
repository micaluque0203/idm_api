select avg(count)
        from(SELECT ip,
        count(*) as count,
        FROM users
        WHERE iso_code='{iso_code}'
        GROUP BY 1) as counts