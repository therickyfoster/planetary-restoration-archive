// scripts/uploadDirectory.mjs
import { NFTStorage } from 'nft.storage'
import { filesFromPath } from 'files-from-path'
import path from 'path'

async function main() {
  const dir = 'public'
  const files = filesFromPath(dir, {
    pathPrefix: path.resolve(dir), 
    hidden: false
  })
  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN })
  const cid = await client.storeDirectory(files)
  console.log('Uploaded CID:', cid)
}

main().catch(err => {
  console.error(err)
  process.exit(1)
})
