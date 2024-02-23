if __name__ == "__main__":
    import uvicorn
    from api.router.router import router
    uvicorn.run(router, host="0.0.0.0", port=8000)