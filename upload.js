import { NFTStorage } from 'nft.storage';
import { filesFromPath } from 'files-from-path';
import path from 'path';

const dir = 'public';

async function main() {
  const files = await filesFromPath(dir, {
    pathPrefix: path.resolve(dir),
    hidden: false,
  });

  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN });
  const cid = await client.storeDirectory(files);
  console.log('✅ Uploaded folder with CID:', cid);
}

main().catch(err => {
  console.error('❌ Upload failed:', err);
  process.exit(1);
});
